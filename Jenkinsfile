pipeline {
  agent any
  
  environment {
    IMAGE_NAME = 'adityawahyuh/notes-app'
    REGISTRY = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS = 'note-app'
  }
  
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    
    stage('Run Unit Tests in Docker') {
      steps {
        bat '''
          docker build -t test-image -f Dockerfile.test .
          docker run --rm test-image
        '''
      }
    }
    
    stage('Build Production Image') {
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
      bat 'docker image prune -f'
    }
    success {
      echo 'Build dan push berhasil!'
    }
    failure {
      echo 'Pipeline gagal! Periksa log untuk detail error.'
    }
  }
}
