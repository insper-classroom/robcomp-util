from setuptools import setup
import os
from glob import glob

package_name = 'robcomp_util'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='somebody very awesome',
    maintainer_email='user@user.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teste_odom_laser = robcomp_util.teste_odom_laser:main',
            'mobilenet_detector = robcomp_util.mobilenet_detector:main',
            'segue_linha = robcomp_util.segue_linha:main',
            'creeper_pub = robcomp_util.creeper_pub:main',
            'action_segue_linha = robcomp_util.action_segue_linha:main',
            'client_segue_linha = robcomp_util.client_segue_linha:main',
            'goto = robcomp_util.goto:main',
            'action_goto = robcomp_util.action_goto:main',
            'client_goto = robcomp_util.client_goto:main',
            'super_client = robcomp_util.super_client:main',
        ],
    },
)