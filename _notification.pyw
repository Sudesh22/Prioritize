import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

#create notifier
nManager = notifications.ToastNotificationManager
app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe'
notifier = nManager.create_toast_notifier(app);

#define your notification as string
tString = """
<toast>
    <visual>
        <binding template='ToastGeneric'>
            <text>Welcome</text>
            <text>This works!</text>
        </binding>
    </visual>
    <actions>

        <action
            content="See more details"
            arguments="action=viewdetails&amp;contentId=351"
            activationType="foreground"/>

        <action
            content="Remind me later"
            arguments="action=remindlater&amp;contentId=351"
            activationType="background"/>

    </actions>
</toast>
"""
#convert notification to an XmlDocument
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)

# print(notifications.TileUpdater)

#display notification
notifier.show(notifications.ToastNotification(xDoc))