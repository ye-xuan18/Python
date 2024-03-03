
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"></li>
        <li class="item-0"></li>
        <li class="item-0"></li>
        <li class="item-0"></li>
        <li class="item-0"></li>
    </ul>
</div>
'''

html = etree.HTML(text)

result = html.xpath('//li')
print(result)