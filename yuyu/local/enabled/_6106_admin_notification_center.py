# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'notification_center'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'admin'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'billing'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'openstack_dashboard.dashboards.yuyu.admin.notification_center.panel.NotificationCenter'
