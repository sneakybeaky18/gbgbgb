import vk_api
from vk_api.audio import VkAudio

vk_session = vk_api.VkApi('+79995005050', 'password')
vk_session.auth()

vkaudio = VkAudio(vk_session)

youraudio = vkaudio.get_iter()
for el in youraudio:
    print(el)