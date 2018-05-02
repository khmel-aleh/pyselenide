*** Settings ***
Suite Setup       WebUI Suite Setup
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Force Tags        common
Default Tags      not_ready
Resource          keywords/webui.config.robot

*** Test Cases ***
Test1
    [Tags]    smoke  debug  01
    [Timeout]  10min
    Google Search               Suite1. Test1
    Google Check Query Text     Suite1

Test2
    [Tags]    smoke  debug  02
    [Timeout]  10min
    Google Search               Suite1. Test2
    Google Check Query Text     Suite2