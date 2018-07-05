*** Settings ***
Suite Setup       WebUI Suite Setup
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Force Tags        common
Default Tags      not_ready
Library           core.libs.ConfigLoader                WITH NAME  ConfigLoader
Library           ui.google.page.GooglePage             WITH NAME  Google
Resource          keywords/webui.config.robot

*** Variables ***
#${BROWSER}=  chrome


*** Test Cases ***
Test1
    [Tags]    smoke  11
    [Timeout]  10min
    Google.Search                   Suite1. Test1
    Google.Check Query Text         Suite1
    Google.check_browser_title      Google
    Google.check_browser_url        google.com

Test2
    [Tags]    smoke  12
    [Timeout]  10min
    Google Search               Suite1. Test2
    google_check_browser_title         Google
    Google Check Query Text     Wrong Query