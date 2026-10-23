pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Python calculator project'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python version'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running calculator unit tests'
                sh 'python3 -m unittest -v test_cal'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Calculator pipeline completed successfully'
            }
        }
    }
}