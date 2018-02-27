<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'miniupnpd';
$app['version'] = '2.5.4';
$app['release'] = '1';
$app['vendor'] = 'Nick Howitt';
$app['packager'] = 'Nick Howitt';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('miniupnpd_app_description');
$app['powered_by'] = array(
    'packages' => array(
        'miniupnpd' => array(
            'name' => 'MiniUPnP',
            'version' => '---',
        ),
    ),
);

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('miniupnpd_app_name');
$app['category'] = lang('base_category_server');
$app['subcategory'] = lang('base_subcategory_virtualization');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['requires'] = array(
    'app-network',
);

$app['core_requires'] = array(
    'app-network-core',
    'miniupnpd',
);

$app['core_directory_manifest'] = array(
    '/var/clearos/miniupnpd' => array(),
);

$app['core_file_manifest'] = array(
    'miniupnpd.php'=> array('target' => '/var/clearos/base/daemon/miniupnpd.php'),
);

$app['delete_dependency'] = array(
    'app-miniupnpd-core',
    'miniupnpd',
);
