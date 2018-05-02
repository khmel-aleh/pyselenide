*** Settings ***
Library           SeleniumLibrary    run_on_failure=Nothing
Library           core
Library           core.loggers
Library           core.libs.ConfigLoader    WITH NAME  ConfigLoader
Library           core.libs.DriverProvider  WITH NAME  DriverProvider
Library           core.utils.utils2robot

*** Keywords ***
WebUI Suite Setup
    Log    "Suite Setup"
    inizialize_driver
    Maximize Browser Window
    Go To  https://google.com

WebUI Suite Teardown
    Log    WebUI teardown
    close browser

Test Teardown
#    Run Keyword If Test Failed    Failed test actions    ${TEST_NAME}
    Failed test actions    ${TEST_NAME}

Test Setup
    ${timestamp}=    Get Time    epoch
    sleep  1
    Set Test Variable    ${TEST_START_TIME}    ${timestamp}
#    Open browser keyword

Capture screenshot
    [Arguments]    ${prefix}
    ${string}=    generate screenshot name    ${prefix}
    Capture Page Screenshot    filename=${string}

Attach webui cli logs
    ${cli_path}=    config.get_cli_logs_path
#    LogSteps.attach_logs_to_robot_from_timestamp    ${TEST_START_TIME}    ${cli_path}

Failed test actions
    [Arguments]    ${test_name}
    Log  Pass
#    Capture screenshot    ${test_name}
#    Attach webui cli logs
#    close_all_browsers