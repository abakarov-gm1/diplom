FROM python:3.10

# Устанавливаем cron и curl
RUN apt-get update && apt-get install -y cron curl

# Добавляем cron-задание в файл crontab 29 дней
# RUN echo "0 0 */29 * * curl -X POST http://fast-api:8000/api/prompts/update >> /var/log/cron.log 2>&1" > /etc/cron.d/my_cron

# Добавляем cron-задание в файл crontab  1 минута
# RUN echo "* * * * * curl -X POST http://fast-api:8000/api/prompts/update >> /var/log/cron.log 2>&1" > /etc/cron.d/my_cron

# 11 часов для сессии
RUN echo "0 */11 * * * curl -X GET http://api-fastapi:8000/super-service/token/new >> /var/log/cron.log 2>&1" > /etc/cron.d/my_cron

# 10 минут для заявок
RUN echo "*/10 * * * * curl -X GET http://api-fastapi:8000/super-service/update/competition >> /var/log/cron.log 2>&1" >> /etc/cron.d/my_cron


# Настраиваем права и регистрируем crontab
RUN chmod 0644 /etc/cron.d/my_cron && crontab /etc/cron.d/my_cron

# Запускаем cron в фоне и следим за логами
CMD cron && tail -f /var/log/cron.log
