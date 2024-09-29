#!/bin/bash
set -e

# WordPress がまだ展開されていない場合にのみ展開
if [ ! -f /var/www/html/index.php ]; then
  echo "Extracting WordPress..."
  tar -xzf /tmp/wordpress-4.7.1.tar.gz -C /var/www/html --strip-components=1
  chown -R www-data:www-data /var/www/html
  echo "WordPress has been extracted."
fi

# Apache の起動
apache2-foreground

