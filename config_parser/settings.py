import os.path

class proxy_opts:
    auto    = 'auto'
    manual  = 'manual'
    noProxy = 'noProxy'

class schedule_opts:
    manual      = 'manual'
    runEvery    = 'runEvery'
    days        = 'days'

class upload_opts:
    manual  = 'manual'
    auto    = 'auto'

timeFormat              = 'hh:mm:ss'
dateFormat              = 'yyyy-MM-ddThh:mm:ss'
runEvery_opts           = ['hour', 'minute']
weekDaysStr             = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
tourDisplayReasons      = ['uncoupling', 'publish']

account_loginType       = 'account/loginType'
account_rememberLogin   = 'account/rememberLogin'
account_username        = 'account/username'
account_password        = 'account/password'
account_runOnStartup    = 'account/runOnStartup'
account_sendErrorLog    = 'account/sendErrorLog'
account_language        = 'account/language'
account_dropboxPrompted = 'account/dropboxPrompted'

oauth_googleExpiry      = 'oauth/googleExpiry'
oauth_facebookExpiry    = 'oauth/facebookExpiry'

compute_rootFolder      = 'compute/rootFolder'
compute_usersFolders    = 'compute/usersFolders'

schedule_runEvery_value = 'schedule/runEvery_value'
schedule_runEvery_unit  = 'schedule/runEvery_unit'
schedule_day_sun        = 'schedule/day_sun'
schedule_day_mon        = 'schedule/day_mon'
schedule_day_tue        = 'schedule/day_tue'
schedule_day_wed        = 'schedule/day_wed'
schedule_day_thu        = 'schedule/day_thu'
schedule_day_fri        = 'schedule/day_fri'
schedule_day_sat        = 'schedule/day_sat'
schedule_day_time       = 'schedule/day_time'
schedule_upload         = 'schedule/upload'
schedule_schedule       = 'schedule/schedule'

vcs_installed_version   = 'vcs/installedVersion'
vcs_new_version         = 'vcs/newVersionInstalled'
vcs_new_version_path    = 'vcs/newVersionPath'
vcs_startup_version     = 'vcs/startupVersion'
vcs_events_notified     = 'vcs/eventsNotified'

status_showFinished     = 'status/showFinished'
status_showPath         = 'status/showPath'
status_showPending      = 'status/showPending'

no_proxy                = 'connection/noProxy'
proxy_server            = 'connection/proxyServer'
proxy_port              = 'connection/proxyPort'
proxy_protocol          = 'connection/proxyScheme'
proxy_is_authenticated  = 'connection/isProxyAuthenticated'
proxy_user              = 'connection/proxyUser'
proxy_password          = 'connection/proxyPassword'
proxy_connection        = 'connection/proxyConnection'
