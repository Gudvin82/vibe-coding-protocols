import * as vscode from 'vscode';

function openRelativeFile(context: vscode.ExtensionContext, relativePath: string) {
  const fileUri = vscode.Uri.joinPath(context.extensionUri, '..', relativePath);
  return vscode.commands.executeCommand('vscode.open', fileUri);
}

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand('vcp.initializeLite', async () => {
      vscode.window.showInformationMessage('Lite initialization is still experimental. Start with START_HERE.md and templates/AGENTS.md.');
    }),
    vscode.commands.registerCommand('vcp.runDoctor', async () => {
      const terminal = vscode.window.createTerminal('VCP Doctor');
      terminal.show();
      terminal.sendText('bash scripts/vibe-check.sh --doctor');
    }),
    vscode.commands.registerCommand('vcp.openStartHere', async () => {
      await openRelativeFile(context, 'START_HERE.md');
    }),
    vscode.commands.registerCommand('vcp.openArchitectureMapTemplate', async () => {
      await openRelativeFile(context, 'templates/ARCHITECTURE_MAP.md');
    })
  );
}

export function deactivate() {
  return undefined;
}
