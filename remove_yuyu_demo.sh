#!/bin/bash

echo "Specify Horizon Location (ex: /etc/horizon): "
read horizon_path
root=`pwd -P`

echo "Removing yuyu demo Symlink"
rm $horizon_path/openstack_dashboard/dashboards/yuyu_demo
rm $horizon_path/openstack_dashboard/local/enabled/_6600_yuyu.py
rm $horizon_path/openstack_dashboard/local/enabled/_6601_admin_billing_panel_group.py
rm $horizon_path/openstack_dashboard/local/enabled/_6602_admin_billing_overview.py
rm $horizon_path/openstack_dashboard/local/enabled/_6603_admin_billing_price_configuration.py
rm $horizon_path/openstack_dashboard/local/enabled/_6604_admin_billing_setting.py
rm $horizon_path/openstack_dashboard/local/enabled/_6604_admin_billing_setting.py
rm $horizon_path/openstack_dashboard/local/enabled/_6605_admin_billing_projects_invoice.py
rm $horizon_path/openstack_dashboard/local/enabled/_6606_admin_notification_center.py
rm $horizon_path/openstack_dashboard/local/enabled/_6607_admin_billing_projects_balance.py

echo "Yuyu Demo Removal Done"