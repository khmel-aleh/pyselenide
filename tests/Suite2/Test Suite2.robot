*** Settings ***
Suite Setup       WebUI Suite Setup
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Force Tags        common
Default Tags      not_ready
Resource          keywords/webui.config.robot

*** Variables ***
${BROWSER}=  chrome

*** Test Cases ***
Test1
    [Tags]    smoke  21
    [Timeout]  10min
    Google Search               Suite2. Test1
    Google Check Query Text     Suite1

Test2
    [Tags]    smoke  22
    [Timeout]  10min
    Google Search               Suite2. Test2
    Google Check Query Text     Suite1