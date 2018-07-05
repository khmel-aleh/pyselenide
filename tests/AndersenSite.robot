*** Settings ***
Resource          tests_resources/webui.config.robot
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Suite Setup       Suite Setup
Force Tags        common
Default Tags      smoke
Library           tests_resources.ui.andersen.pages.index.AndersenSite  WITH NAME  AndersenSite

*** Test Cases ***
Check for static headers on page scrolls
    [Documentation]  Проверить появления статического хедера при скролле страницы
    [Tags]    smoke  C4121844  andersen  no_run
    [Timeout]  10min
    Do Search


Check the hover efect link "Staff Augmentation"
    [Documentation]  Проверить ховер ефект ссылки "Staff Augmentation"
    [Tags]    smoke  C4121849  andersen  no_run
    [Timeout]  10min
    Hover Find Develops

Check the clickability of the link "Project Development"
    [Documentation]  Проверить кликабельность ссылки "Project Development"
    [Tags]    smoke  C4121860  andersen
    [Timeout]  10min
    Call method             ${AndersenSite.find_devs_link}      click
    Check Browser Url       https://newdsgn.andersenlab.com/find-developers.php

*** Keywords ***
Suite Setup
    WebUI Suite Setup
    Go To   https://newdsgn.andersenlab.com
    ${AndersenSite}=        Get Library Instance        AndersenSite
    Set Suite Variable      ${AndersenSite}
    ${Browser}=             Get Library Instance        DriverProvider
    Set Suite Variable      ${Browser}
