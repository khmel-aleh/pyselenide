*** Settings ***
Resource          keywords/webui.config.robot
Suite Setup       WebUI Suite Setup
Suite Teardown    WebUI Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Force Tags        common
Default Tags      smoke
Library           ui.selenium_demo.pages.index.SeleniumDemo

*** Test Cases ***
Drag And Drop Action
    [Tags]    smoke  draganddrop  selenium_demo  no_run
    [Timeout]  10min
    Go To   http://the-internet.herokuapp.com/drag_and_drop
    do_drag_and_drop

Hover Action
    [Tags]    smoke  hover  selenium_demo  no_run
    [Timeout]  10min
    Go To   http://the-internet.herokuapp.com/hovers
    hover

Key Press Action
    [Tags]    smoke  key_press  selenium_demo
    [Timeout]  10min
    Go To   http://the-internet.herokuapp.com/hovers
    Go To   http://the-internet.herokuapp.com/key_presses
    Go To   https://tut.by
#    Key Press  D