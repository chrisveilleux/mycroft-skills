pipeline {
    agent any
    options {
        // Running builds concurrently could cause a race condition with
        // building the Docker image.
        disableConcurrentBuilds()
    }
    stages {
        // Run the build in the against the dev branch to check for compile errors
        stage('Run Integration Tests') {
            when {
                anyOf {
                    branch 'feature/voight-kampff'
                    changeRequest()
                }
            }
            steps {
                sh 'docker build --build-arg branch_name=96.02 --build-arg platform=mycroft_mark_1 --build-arg pull_request=PR-1 -t voight-kampff-skill:test .'
//                 echo 'Running Tests'
//                 timeout(time: 10, unit: 'MINUTES')
//                 {
//                     sh 'docker run \
//                         -v "$HOME/voight-kampff:/root/.mycroft" \
//                         --device /dev/snd \
//                         -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
//                         -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
//                         -v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
//                         mycroft-core:${BRANCH_ALIAS}'
//                 }
            }
//             post {
//                 always {
//                     echo 'Report Test Results'
//                     sh 'mv $HOME/voight-kampff/allure-result allure-result'
//                     script {
//                         allure([
//                             includeProperties: false,
//                             jdk: '',
//                             properties: [],
//                             reportBuildPolicy: 'ALWAYS',
//                             results: [[path: 'allure-result']]
//                         ])
//                     }
//                     unarchive mapping:['allure-report.zip': 'allure-report.zip']
//                     sh (
//                         label: 'Publish Report to Web Server',
//                         script: '''scp allure-report.zip root@157.245.127.234:~;
//                             ssh root@157.245.127.234 "unzip -o ~/allure-report.zip";
//                             ssh root@157.245.127.234 "rm -rf /var/www/voight-kampff/${BRANCH_ALIAS}";
//                             ssh root@157.245.127.234 "mv allure-report /var/www/voight-kampff/${BRANCH_ALIAS}"
//                         '''
//                     )
//                     echo 'Report Published'
//                 }
//             }
        }
    }
//     post {
//         cleanup {
//             sh(
//                 label: 'Docker Container and Image Cleanup',
//                 script: '''
//                     docker container prune --force;
//                     docker image prune --force;
//                 '''
//             )
//         }
//         always {
//             githubNotify context: 'Voight Kampff Test...', description: 'Static Check Tests Passed', status: 'SUCCESS'
//         }
//     }
}
