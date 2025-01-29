pipeline {
    agent {
        docker {
            image 'python:3.10-slim' // Use Python Docker image for the build environment
        }
    }
    triggers {
        githubPush() // Trigger the pipeline on a GitHub push event
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the repository from GitHub
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    sh 'docker build -t website-tester .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Run the Docker container to execute Pytest and generate the report
                script {
                    sh 'docker run --rm -v ${WORKSPACE}:/app website-tester'
                }
            }
        }
        stage('Archive Report') {
            steps {
                // Archive the test report file
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
        stage('Publish Test Results') {
            steps {
                // Publish test results in Jenkins (requires JUnit plugin)
                junit 'report.html'
            }
        }
    }
    post {
        always {
            // Clean up unused Docker resources after the build
            sh 'docker system prune -f'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs and report.'
        }
    }
}
