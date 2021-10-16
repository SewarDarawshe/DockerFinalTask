pipeline {


   
      agent any



    stages {



        stage('Cloning our Git') {



            steps {

                git 'https://github.com/SewarDarawshe/DockerFinalTask.git'
               }


        }


        stage('Building our image') {

            steps {

                sh 'docker build -t dockerfinaltask:webapp .' 
                  sh 'docker tag pythonproject sewardrawshe/dockerfinaltask:webapp'
                sh 'docker tag pythonproject sewardrawshe/dockerfinaltask:$BUILD_NUMBER'
               

            }

        }



        stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "dockerhub_id", url: "" ]) {
          sh  'docker push sewardrawshe/dockerfinaltask:webapp'
          sh  'docker push sewardrawshe/dockerfinaltask:$BUILD_NUMBER' 
        }
                  
          }
        }
      

    }



} 
