# ML services Project

Этот проект направлен на повышение безопасности пожилых людей с помощью приложения, использующего методы машинного обучения.

## Machine Learning Models

Были использованы модели:

1. **SVM Model:** F1 - 0.75
2. **Random Forest Model:** F1 - 0.78
3. **Logistic Regression Model:** F1 - 0.83

Процесс обучения моделей можно посмотреть здесь: `/api/models/training.ipynb`.

## Getting Started 🛠️

### Prerequisites

- [Docker](https://www.docker.com/get-started)


### Running the Project ▶️

1. Clone the repository:

   ```bash
   git clone https://github.com/KaroUniform/itmo-dev
   cd itmo-dev
   ```
2. Build and run the project using Docker Compose:
   ```
   sudo docker-compose up -d
   ```
3. Demo and Documentation

- **Demo** will be [here](http://172.21.0.2:8501).
- **API Documentation** will be [here](http://ml_services_fastapi_1:8502/docs).
