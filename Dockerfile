# Run skill changes against the last major release of Mycroft Core but install
# the latest version of all skills.
ARG major_release
FROM voight-kampff-mark-1:${major_release}
ARG pull_request
ARG platform
ARG branch_name
WORKDIR /opt/mycroft/mycroft-core
COPY test-requirements.txt .
RUN .venv/bin/python -m pip install -r test-requirements.txt
COPY voight_kampff.py .
RUN .venv/bin/python voight_kampff.py --pull-request $pull_request --platform $platform
RUN python -m test.integrationtests.voight_kampff.test_setup --config test_skill.yml --platform $platform --branch $major_release
# Setup and run the integration tests
#ENV PYTHONPATH /opt /mycroft/mycroft-core/
#WORKDIR /opt/mycroft/mycroft-core/test/integrationtests/voight_kampff
#ENTRYPOINT ["./run_test_suite.sh"]
