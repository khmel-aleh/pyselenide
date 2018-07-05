*** Settings ***
Resource          tests_resources/webui.config.robot
Suite Setup       WebUI Suite Setup
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Force Tags        common
Default Tags      smoke
Library           tests_resources.ui.onliner.pages.index.Onliner

*** Test Cases ***
Drag And Drop Action
    [Tags]    smoke  draganddrop  onliner
    [Timeout]  10min
    Go To   https://onliner.by
    Do Search
