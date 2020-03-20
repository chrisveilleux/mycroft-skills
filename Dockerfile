# Run skill changes against the last major release of Mycroft Core but install
# the latest version of all skills.
ARG branch_name
FROM voight-kampff-mark-1:${branch_name}
ARG pull_request
ARG platform
WORKDIR /opt/mycroft/mycroft-core
COPY test-requirements.txt .
RUN .venv/bin/python -m pip install -r test-requirements.txt
COPY voight_kampff.py .
RUN .venv/bin/python voight_kampff.py --pull-request $pull_request --platform $platform
RUN python -m test.integrationtests.voight_kampff.test_setup --config test_skill.yml --platform $platform
