FROM php:7.0-apache

# 必要なPHPモジュールとライブラリをインストール
# Debian Stretch のアーカイブリポジトリを使うように設定
RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libxml2-dev \
    zlib1g-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) mysqli gd \
    && rm -rf /var/lib/apt/lists/*


# WordPress 4.7.1 アーカイブをコンテナに追加
COPY wordpress-4.7.1.tar.gz /tmp/wordpress-4.7.1.tar.gz

# entrypoint.sh スクリプトをコンテナに追加し、実行権限を付与
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# entrypoint を指定
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# ポート 80 を公開
EXPOSE 80

