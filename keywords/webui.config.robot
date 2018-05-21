*** Settings ***
Library           SeleniumLibrary    run_on_failure=Nothing
Library           core_base.libs.ConfigLoader    WITH NAME  ConfigLoader
Library           core_base.libs.DriverProvider  WITH NAME  DriverProvider
Library           core_base.loggers
Library           core_base.utils.utils2robot

*** Keywords ***
WebUI Suite Setup
    Log    "Suite Setup"
    inizialize_driver
    Maximize Browser Window

WebUI Suite Teardown
    Log    WebUI teardown
    close browser

Test Teardown
#    Run Keyword If Test Failed    Failed test actions    ${TEST_NAME}
    Failed test actions    ${TEST_NAME}

Test Setup
    ${timestamp}=    Get Time    epoch
    Set Test Variable    ${TEST_START_TIME}    ${timestamp}

Capture screenshot
    [Arguments]    ${prefix}
    ${string}=    generate screenshot name    ${prefix}
    Capture Page Screenshot    filename=${string}

Attach webui cli logs
    ${cli_path}=    config.get_cli_logs_path

Failed test actions
    [Arguments]    ${test_name}
    Log  Pass
#    Capture screenshot    ${test_name}
#    Attach webui cli logs
#    close_all_browsers