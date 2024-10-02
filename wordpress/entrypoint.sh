#!/bin/bash
set -e

# WordPress がまだ展開されていない場合にのみ展開
if [ ! -f /var/www/html/index.php ]; then
  echo "Extracting WordPress..."
  tar -xzf /tmp/wordpress-4.7.1.tar.gz -C /var/www/html --strip-components=1
  chown -R www-data:www-data /var/www/html
  echo "WordPress has been extracted."
fi

# WordPress 自動アップデート抑止用の設定を wp-config.php に追加
if [ -f /var/www/html/wp-config.php ]; then
  if ! grep -q "define('AUTOMATIC_UPDATER_DISABLED', true);" /var/www/html/wp-config.php; then
    echo "Disabling automatic updates in wp-config.php..."
    echo "define('AUTOMATIC_UPDATER_DISABLED', true);" >> /var/www/html/wp-config.php
  fi
else
  echo "Creating wp-config.php with automatic updates disabled..."
  cat <<EOL > /var/www/html/wp-config.php
<?php
define('AUTOMATIC_UPDATER_DISABLED', true);
EOL
  chown www-data:www-data /var/www/html/wp-config.php
fi

# Apache の起動
apache2-foreground

