# Script Name:                  Ops 401d8 Lab 4
# Author:                       David Prutch
# Date of latest revision:      07/13/2023
# Purpose:                      Powershell automation script to change password complexity requirements and disable SMBv1 protocol.

# Declaration of variables

# Declaration of functions


# Main
Install-Module -Name SecurityPolicyDsc -Force

# Import the SecurityPolicyDsc module
Import-Module SecurityPolicyDsc

# Define the configuration
$configurationData = @{
    AllNodes = @(
        @{
            NodeName = 'localhost'
            PSDscAllowPlainTextPassword = $true
        }
    )
}

$configuration = @{
    LocalConfigurationManager = @{
        ConfigurationMode = 'ApplyOnly'
        RebootNodeIfNeeded = $false
    }
    SecurityPolicy = @{
        PasswordComplexity = @{
            Ensure = 'Present'
            Value = $true
        }
    }
}

# Apply the configuration
Start-DscConfiguration -Path .\LocalSecurityPolicy -Wait -Verbose -Force -ConfigurationData $configurationData -ConfigurationData $configuration

# Disable SMB1 Protocol
Set-SmbServerConfiguration -EnableSMB1Protocol $false