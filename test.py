# import requests
# from random import choice
#
# URL = 'http://127.0.0.1:5000/posts/create'
#
# post_titles = ['Post', 'Another Post', 'Test Post', 'Properties Post']
# second_post_titles = ['about monkeys', 'about birds', 'about cars', 'about numbers', 'about mathematical logic']
#
# body = [
#   'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sed lectus vel leo hendrerit efficitur eu eget arcu. Duis sit amet augue non augue vulputate mattis. Morbi id ex id tellus vestibulum porttitor. Nullam ultrices rhoncus ex. Sed euismod sit amet nunc nec efficitur. Donec velit nisi, mollis in dictum a, auctor maximus nibh. Suspendisse eu lobortis ligula. Nulla vitae felis eros. Morbi nec orci dolor. Mauris suscipit magna quis sem tempor, hendrerit mattis purus facilisis. Sed diam turpis, aliquet ac placerat vel, tempus et purus. Sed aliquet odio sit amet nulla vestibulum aliquam. Morbi in tempor lectus. Integer et tortor purus.',
#   'Suspendisse at gravida mauris. Sed sed sapien eget ex mattis mattis. In a magna et risus eleifend vestibulum a accumsan ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse at diam commodo, finibus enim nec, rutrum leo. Maecenas laoreet ultricies elit, vel posuere tellus luctus eu. Morbi non mattis eros. Vivamus eget pulvinar purus. Vivamus fringilla arcu quis ex rutrum, eget blandit felis pharetra. Etiam felis urna, porttitor ultrices luctus sed, finibus nec mauris. Vivamus eu nisi vel tortor volutpat dapibus. Nunc fringilla libero ex, nec facilisis leo laoreet eu. Nunc egestas eleifend turpis ut mollis.',
#   'Sed eu felis ultrices, tempus ligula at, placerat ipsum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut eleifend dolor massa, in hendrerit mi consequat at. Quisque et ipsum nec mauris efficitur lacinia. Vestibulum diam purus, ultrices ut blandit vitae, dapibus vitae justo. Morbi iaculis enim eu vehicula tincidunt. Suspendisse varius dolor orci, sed mollis neque semper sed. Donec eu orci elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sodales eget nulla non rhoncus. Nulla in mollis augue. Nullam posuere quam at felis ornare gravida. Quisque consequat neque nibh, a mollis augue cursus molestie.',
#   'Donec tincidunt tempus lectus eu aliquet. Mauris blandit velit sit amet ex rutrum, cursus maximus odio tristique. Integer tincidunt ante sed egestas maximus. Phasellus hendrerit ex justo, a placerat augue tincidunt eu. Morbi ut iaculis quam. Mauris porttitor velit nulla, eget condimentum dolor cursus eget. Nullam faucibus purus ac mauris ultricies, eu porttitor ante tincidunt. Etiam pulvinar eu ligula at rutrum. Pellentesque molestie bibendum mi quis dictum. Vestibulum elementum augue velit, nec tincidunt neque vulputate id. Donec id accumsan est. Nulla sollicitudin vel purus sed auctor. Praesent lacinia at orci vehicula facilisis. Cras quis augue mollis, aliquet metus vel, varius est. Vivamus eu magna efficitur, malesuada sapien a, rhoncus purus. Cras accumsan, diam vel vestibulum sollicitudin, magna purus volutpat sem, ac aliquam felis magna eget ligula.',
#   'Quisque dapibus rutrum mauris, eget lacinia neque ultricies non. Etiam nec ante ligula. Fusce ac turpis eget mi mattis ultricies. Cras feugiat nibh eu magna porttitor, tristique dignissim justo sagittis. Curabitur a sem sed nulla tempus rhoncus. Pellentesque eros felis, aliquet ut maximus in, blandit at neque. Aliquam id massa et odio porta commodo. Proin pharetra efficitur elit vel porta. In hac habitasse platea dictumst. Ut nec leo ullamcorper, posuere augue at, varius justo. Aliquam sit amet aliquam arcu, at dapibus arcu. Nam sit amet ex vulputate, volutpat est eleifend, venenatis libero.'
# ]
#
# with requests.session() as session:
#   for i in range(5):
#     data = {
#       'title': choice(post_titles) + ' ' + choice(second_post_titles),
#       'body': choice(body)
#     }
#
#     session.post(URL, data)

import _sha512
print(_sha512.sha512('stardewvalley'.encode()).digest())

