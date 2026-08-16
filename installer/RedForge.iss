#define MyAppName "RedForge"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Arpit Toppo"
#define MyAppExeName "RedForge.exe"

[Setup]
AppId={{db0b643e-fdb0-4be9-acd6-0aa1ffd79e71}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\RedForge
DefaultGroupName=RedForge

OutputDir=..\dist
OutputBaseFilename=RedForge-Setup

SetupIconFile=..\assets\redforge.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

Compression=lzma
SolidCompression=yes

PrivilegesRequired=admin

[Files]
Source: "..\dist\RedForge\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\RedForge"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\RedForge"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch RedForge"; Flags: nowait postinstall skipifsilent