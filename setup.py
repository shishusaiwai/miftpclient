from setuptools import setup, find_packages
setup(name='miftpclient',
      version="0.3",
      description="connect to your xiaomi phone's ftp server automatically.",
      author="cong liu",
      author_email="shishusaiwai@vip.qq.com",
      license="GPL",
      packages=find_packages(),
      entry_points={"console_scripts": ["miftpclient = miftpclient.main:main"]})
