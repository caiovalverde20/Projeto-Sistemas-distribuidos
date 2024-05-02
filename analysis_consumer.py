from kafka import KafkaConsumer
import json
from datetime import datetime
import collections

analysis_consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='event-analysis-group',  # Um novo group_id para o consumer de análise
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Estrutura para armazenamento e análise de eventos
event_analysis_log = collections.defaultdict(list)

def analyze_events():
    print("Iniciando análise de eventos...")
    for message in analysis_consumer:
        event_data = message.value.get('value')
        event_type = event_data.get('message').lower().split()[0] + " " + event_data.get('message').lower().split()[1] # extrai o tipo de evento

        timestamp = event_data.get('timestamp') 
        event_analysis_log[event_type].append(timestamp)

        # Análise de frequência e padrões temporais
        print(f"Análise para {event_type}: {len(event_analysis_log[event_type])} eventos até agora.")
        print(f"Timestamps dos últimos eventos: {event_analysis_log[event_type][-5:]}")  # Exibe os últimos 5 eventos

        # Medir duração entre eventos do mesmo tipo
        if len(event_analysis_log[event_type]) > 1:
            last_event_time = datetime.fromisoformat(event_analysis_log[event_type][-2])
            current_event_time = datetime.fromisoformat(timestamp)
            duration = current_event_time - last_event_time
            print(f"Tempo desde o último evento {event_type}: {duration.total_seconds()} segundos")

        # Análise de tentativas de login falhas
        if "failed" in event_type:
            event_analysis_log['failed_login_attempts'].append(timestamp)
            print(f"Tentativas de login falhas: {len(event_analysis_log['failed_login_attempts'])}")

        # Calculando taxas de sucesso e falha para logins
        if 'login' in event_type:
            success_count = len(event_analysis_log['login successful'])
            failed_count = len(event_analysis_log['login failed'])
            if failed_count + success_count > 0:
                success_rate = (success_count / (failed_count + success_count)) * 100
                print(f"Taxa de sucesso de login: {success_rate:.2f}%")

        # Análise específica para eventos de erro
        if "error occurred" in event_type:
            error_count = len(event_analysis_log[event_type])
            print(f"Total de eventos de erro: {error_count}")

            if error_count > 1:
                # Calcula o tempo médio entre erros
                error_times = [datetime.fromisoformat(t) for t in event_analysis_log[event_type]]
                error_intervals = [(error_times[i] - error_times[i - 1]).total_seconds() for i in range(1, len(error_times))]
                average_interval = sum(error_intervals) / len(error_intervals)
                print(f"Tempo médio entre eventos de erro: {average_interval:.2f} segundos")

        print("\n")
if __name__ == '__main__':
    analyze_events()