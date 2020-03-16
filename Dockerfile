# Run skill changes against the last major release of Mycroft Core but install
# the latest version of all skills.
ARG branch_name
FROM voight-kampff-mark-1:${branch_name}
ARG pull_request
ARG platform
WORKDIR /opt/mycroft/mycroft-core/.venv
COPY test-requirements.txt .
RUN bin/python -m pip install -r test_requirements.txt
RUN export SKILL=bin/python -m voight_kampff --pull-request $pull_request --platform $platform
RUN msm install ${skill} -b ${BRANCH_NAME}
WORKDIR /opt/mycroft/mycroft-core
RUN python -m test.integrationtests.voight_kampff.test_setup --tested-skills $skill --platform $platform
