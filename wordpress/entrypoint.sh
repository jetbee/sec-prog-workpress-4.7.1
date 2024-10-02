#!/bin/bash
set -e

# WordPress がまだ展開されていない場合にのみ展開
if [ ! -f /var/www/html/index.php ]; then
  echo "Extracting WordPress..."
  tar -xzf /tmp/wordpress-4.7.1.tar.gz -C /var/www/html --strip-components=1
  chown -R www-data:www-data /var/www/html
  echo "WordPress has been extracted."

  # wp-config-sample.php に自動アップデート抑止の設定を追加
  if [ -f /var/www/html/wp-config-sample.php ]; then
    echo "Modifying wp-config-sample.php to disable automatic updates..."
    if ! grep -q "define('AUTOMATIC_UPDATER_DISABLED', true);" /var/www/html/wp-config-sample.php; then
      echo "define('AUTOMATIC_UPDATER_DISABLED', true);" >> /var/www/html/wp-config-sample.php
    fi
  fi
fi

# Apache の起動
apache2-foreground

