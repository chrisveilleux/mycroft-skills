from argparse import ArgumentParser
# from pathlib import Path

# import docker
import requests
from github import Github

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "--pull-request",
    default=None,
    help='The Pull Request to be tested.'
)
arg_parser.add_argument(
    "--platform",
    default='mycroft_mark_1',
    help='The Pull Request to be tested.'
)
args = arg_parser.parse_args()

pr_number = int(args.pull_request.strip('PR-'))
g = Github('chrisveilleux', 'uq%Bd3GzFA3JEkH*7tf3')
repo = g.get_repo('chrisveilleux/mycroft-skills')
pr = repo.get_pull(pr_number)

# Determine if the PR is for a new or updated skill by inspecting the PR diff
pr_diff = requests.get(pr.diff_url)
diff_file_name = None
skill_submodule_name = None
for line in pr_diff.text.split('\n'):
    #  The line indicating the file being compared looks like this:
    #    diff --git a/<file name> b/<file name>
    if line.startswith('diff --git a/'):
        words = line.split()
        diff_file_name = words[2].strip('a/')
    # If a file contains a subproject commit hash it represents a skill
    if line.startswith('+Subproject commit '):
        skill_submodule_name = diff_file_name
        break

print('export SKILL_NAME=', skill_submodule_name)

# # There are files in the repository that are not skill subprojects.
# # No need to run the tests if a skill is not changed.
# if skill_submodule_name is not None:
#     docker_image_name = 'voight-kampff-skill:' + skill_submodule_name
#     docker_client = docker.from_env()
#     docker_client.build(
#         path=str(Path.cwd()),
#         tag=docker_image_name,
#         buildargs=dict(skill=skill_submodule_name, platform=args.platform)
#     )
#     volumes = {
#         '$HOME/voight-kampff/identity': dict(
#             bind='/root/.mycroft/identity',
#             mode='rw'
#         ),
#         '$HOME/voight-kampff/': dict(bind='/root/allure', mode='rw'),
#     }
#     docker.client.run(
#         image=docker_image_name,
#         command=[
#             '-f allure_behave.formatter:AllureFormatter',
#             '-o /root/allure/allure-result',
#             '--tags ~@xfail'
#         ]
#     )
