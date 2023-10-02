#!/bin/bash

echo "Specify Horizon Location (ex: /etc/horizon): "
read horizon_path
root=`pwd -P`

echo "Creating Symlink"
ln -sf $root/yuyu_demo $horizon_path/openstack_dashboard/dashboards
ln -sf $root/yuyu_demo/local/enabled/_6600_yuyu_demo.py $horizon_path/openstack_dashboard/local/enabled/_6600_yuyu_demo.py
ln -sf $root/yuyu_demo/local/enabled/_6601_admin_billing_panel_group.py $horizon_path/openstack_dashboard/local/enabled/_6601_admin_billing_panel_group.py
ln -sf $root/yuyu_demo/local/enabled/_6602_admin_billing_overview.py $horizon_path/openstack_dashboard/local/enabled/_6602_admin_billing_overview.py
ln -sf $root/yuyu_demo/local/enabled/_6603_admin_billing_price_configuration.py $horizon_path/openstack_dashboard/local/enabled/_6603_admin_billing_price_configuration.py
ln -sf $root/yuyu_demo/local/enabled/_6604_admin_billing_setting.py $horizon_path/openstack_dashboard/local/enabled/_6604_admin_billing_setting.py
ln -sf $root/yuyu_demo/local/enabled/_6604_admin_billing_setting.py $horizon_path/openstack_dashboard/local/enabled/_6604_admin_billing_setting.py
ln -sf $root/yuyu_demo/local/enabled/_6605_admin_billing_projects_invoice.py $horizon_path/openstack_dashboard/local/enabled/_6605_admin_billing_projects_invoice.py
ln -sf $root/yuyu_demo/local/enabled/_6606_admin_notification_center.py $horizon_path/openstack_dashboard/local/enabled/_6605_admin_notification_center.py
ln -sf $root/yuyu_demo/local/enabled/_6607_admin_billing_projects_balance.py $horizon_path/openstack_dashboard/local/enabled/_6607_admin_billing_projects_balance.py

echo "Symlink Creation Done"
echo "Now you can configure and use yuyu dashboard"