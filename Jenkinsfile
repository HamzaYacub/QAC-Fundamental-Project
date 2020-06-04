pipeline {

    agent any

    stages {
        stage('Enable all scripts to become executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        stage('Get the environment ready') {
            steps {
                sh './script/beforeinstallation.sh'
                sh './script/installation.sh'
            }
        }
        stage('Run the application') {
            steps {
                sh 'sudo systemctl restart flask.service'
                sh 'sudo systemctl status flask.service'
            }
        }
    }
}