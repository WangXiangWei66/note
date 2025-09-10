from .default import DevelopmentConfig
from .default import ProductConfig


# 把两个不同环境的配置和字符串映射起来
map_config = {
    'develop': DevelopmentConfig,
    'product': ProductConfig
}
