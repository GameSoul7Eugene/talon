import sys
import winreg
from utilities.util_logger import logger
from utilities.util_error_popup import show_error_popup
from utilities.util_modify_registry import set_value



def main():
    registry_modifications = [
        """
            Disabling different types of annoyances
        """
        
        # Turn off File Explorer Ads
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "ShowSyncProviderNotifications", winreg.REG_DWORD, 0),
        
        # Don't show (ads) recommendations for tips, shortcuts, new apps, and more on Start Menu
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "Start_IrisRecommendations", winreg.REG_DWORD, 0),
        
        # Don't show Microsoft account-related notifications on Start Menu
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "Start_AccountNotifications", winreg.REG_DWORD, 0),
        
        # Don't suggest ways to get the most out of Windows and finish setting up this device
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\UserProfileEngagement",
        "ScoobeSystemSettingEnabled", winreg.REG_DWORD, 0),
        
        # Disable "Tailored Experiences"
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Privacy",
        "TailoredExperiencesWithDiagnosticDataEnabled", winreg.REG_DWORD, 0),
        
        # Disable "Notification Suggestions"
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.ActionCenter.SmartOptOut",
        "Enabled", winreg.REG_DWORD, 0),
        
        """
            Disabling all possible ContentDeliveryManager settings
        """
        
        # Don't get (ads) fun facts, tips, tricks, and more on the lock screen
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "RotatingLockScreenOverlayEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-338387Enabled", winreg.REG_DWORD, 0),
        
        # Don't show (ads) suggested content in the Settings app
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-338393Enabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-353694Enabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-353696Enabled", winreg.REG_DWORD, 0),
        
        # Don't get general tips and suggestions when using Windows
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-338389Enabled", winreg.REG_DWORD, 0),
        
        # Turn off Windows welcome experience ads
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-310093Enabled", winreg.REG_DWORD, 0),
        
        # Other yet unnamed ContentDeliveryManager options to disable as well
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "ContentDeliveryAllowed", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "FeatureManagementEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "OEMPreInstalledAppsEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "PreInstalledAppsEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "PreInstalledAppsEverEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SilentInstalledAppsEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SoftLandingEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-338388Enabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContent-353698Enabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SubscribedContentEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager",
        "SystemPaneSuggestionsEnabled", winreg.REG_DWORD, 0),
        
        """
            Interface
        """
        
        # Align taskbar to the left
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "TaskbarAl", winreg.REG_DWORD, 0),
        
        # Show extensions for known file types
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "HideFileExt", winreg.REG_DWORD, 0),
        
        # Open File Explorer to This PC
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "LaunchTo", winreg.REG_DWORD, 1),
        
        # Set default app mode to dark
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
        "AppsUseLightTheme", winreg.REG_DWORD, 0),
        
        # Set default Windows mode to dark
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
        "SystemUsesLightTheme", winreg.REG_DWORD, 0),
        
        # Don't animate windows when minimizing and maximizing
        (winreg.HKEY_CURRENT_USER,
        r"Control Panel\Desktop\WindowMetrics",
        "MinAnimate", winreg.REG_DWORD, 0),
        
        # Show window contents while dragging
        (winreg.HKEY_CURRENT_USER,
        r"Control Panel\Desktop",
        "DragFullWindows", winreg.REG_SZ, "1"),
        
        """
            Misc.
        """
        
        # Set shortest character repeat delay
        (winreg.HKEY_CURRENT_USER,
        r"Control Panel\Keyboard",
        "KeyboardDelay", winreg.REG_SZ, "0"),
        
        # Disable "Fast Startup"
        (winreg.HKEY_LOCAL_MACHINE,
        r"SYSTEM\CurrentControlSet\Control\Session Manager\Power",
        "HiberbootEnabled", winreg.REG_DWORD, 0),
        
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\GameDVR",
        "AppCaptureEnabled", winreg.REG_DWORD, 0),
        (winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR",
        "Value", winreg.REG_DWORD, 0),
        (winreg.HKEY_CURRENT_USER,
        r"Control Panel\Desktop",
        "MenuShowDelay", winreg.REG_SZ, "0"),
        (winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
        "ExtendedUIHoverTime", winreg.REG_DWORD, 1)
    ]
    for hive, key_path, name, value_type, value in registry_modifications:
        try:
            logger.info(f"Applying registry tweak: {key_path}\\{name} = {value!r} (type={value_type})")
            set_value(hive, key_path, name, value, value_type)
            logger.info(f"Successfully set {name}")
        except Exception as e:
            logger.error(f"Failed to apply registry tweak {name}: {e}")
            try:
                show_error_popup(
                    f"Failed to apply registry tweak:\n{key_path}\\{name}\n\n{e}",
                    allow_continue=False
                )
            except Exception:
                pass
            sys.exit(1)

    logger.info("All registry tweaks applied successfully.")



if __name__ == "__main__":
    main()