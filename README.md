## Multi-Cased Crawler

Web Crawling 작업을 정형/효율화 하기 위한 Multi-Cased Crawler 입니다.
기존 Selenium을 이용한 Crawling 작업은 Element 하나를 도출/저장/처리하는 과정에서 Crawler를 다루는 함수가 복잡해지고 Selenium 이용을 위한 다양한 함수와 Attribute들을 외워야 할 필요가 있었습니다.

본 프로젝트는 Selenium 이용을 단순화하여 하나의 함수에서 모든 기능을 이용 가능하게 하고, 최종적으로는 JSON 문서의 형태로 명령어를 전달하여 일련의 크롤링 과정을 자동화 하는 것이 목표입니다.

현재 사용가능한 기능은 아래와 같습니다. 

        """
        method :
             - 0 (element)- get an element
             - 1 (elements) - will be supported at version 1.0

        scr_form :
            - 0 (id)  find element by element id
            - 1 (class) : find element by element class
            - 2 (tag name) : find element by tag name
            - 3 (xpath) : find element by xpath
            - 4 (css selector) : find element by css selector

        scr_form_param : parameters using at each 'find_element' method
            - ex) find by tag name <p> -> 'p'

        action :
            - 0 (click) : click() method's parameter
            - 1 (send_key) : use [send keys()] method's parameter
            - 2 (mouse) : will be supported with version 1.0
            - 3 (wheel) : will be supported with version 1.0
            - 4 (get text) : return current element's text
            - 5 (get_attribute) : return current element's attribute

        action_param : parameters using at each action
            - ex) using [action = 2] and [action_param = Keys.ENTER] will be [send_keys(Keys.ENTER)]

        action_options : will be supported at version 1.0

        return:
        """
method:
- 0 = 단일 element 파싱
- 1 = 복수의 element 파싱

scr_form:
- 0 = id 기반 element 탐색
- 1 = class 기반 element 탐색
- 2 = tag name 기반 element 탐색
- 3 = xpath 기반 element 탐색
- 4 = css 기반 element 탐색

scr_form_param:
- find_element parameter에 전달할 element 탐색값

action_param:
- 0 = 클릭 method
- 1 = send_keys()를 이용한 키값 전달(ex: Keys.ENTER)
- 2 = mouse 기능, 미지원
- 3 = wheel 기능, 미지원
- 4 = element별 text값 파싱
- 5 = element 별 HTML attribute값 반환

action_param:
- 상단 action_param의 attribute에 전달할 parameter(ex: Keys.ENTER)