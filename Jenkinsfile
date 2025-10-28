pipeline {
  agent any
  
  environment {
    IMAGE_NAME = 'adityawahyuh/notes-app'
    REGISTRY = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS = 'notes-app'
    PATH = "C:\\Python312;C:\\Python312\\Scripts;${env.PATH}"
  }
  
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    
    stage('Install Dependencies') {
      steps {
        bat '''
          python --version
          python -m venv venv
          call venv\\Scripts\\activate.bat
          pip install -r requirements.txt
        '''
      }
    }
    
    stage('Unit Test') {
      steps {
        bat '''
          call venv\\Scripts\\activate.bat
          pytest test_app.py -v --tb=short
        '''
      }
    }
    
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }
    
    stage('Push Docker Image') {
      steps {
        script {
          docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
            def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
            docker.image(tag).push()
            docker.image(tag).push('latest')
          }
        }
      }
    }
  }
  
  post {
    always {
      echo 'Pipeline selesai dijalankan'
    }
    success {
      echo 'Build dan push berhasil!'
    }
    failure {
      echo 'Pipeline gagal! Periksa log untuk detail error.'
    }
  }
}
