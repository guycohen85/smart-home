# SSH access to Home Assistant

Use a separate key from the GitHub one — never reuse a key across source control and infrastructure access. Generate it under `~/.ssh`, not inside the repo folder (the repo lives under OneDrive sync, so anything placed there — even if gitignored — still gets uploaded to the cloud).

1. Generate a dedicated key pair:
   ```
   ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_home_assistant -C "home assistant access"
   ```
2. In Home Assistant, add-on **Terminal & SSH**:
   - Configuration tab: add the contents of `id_ed25519_home_assistant.pub` to `authorized_keys`.
   - Network tab: toggle "Show disabled ports" and set an SSH port (e.g. `22222`).
   - Configuration tab, **Server** option group: enable `tcp_forwarding` (required for VS Code Remote-SSH to work; plain `ssh`/terminal use doesn't need it).
   - Save and restart the add-on.
3. Add to `~/.ssh/config`:
   ```
   Host home-assistant
       HostName 192.168.1.223
       User root
       Port 22222
       IdentityFile ~/.ssh/id_ed25519_home_assistant
       IdentitiesOnly yes
   ```
4. Verify:
   ```
   ssh home-assistant "echo connected"
   ```
5. In VS Code: "Remote-SSH: Connect to Host" → type `home-assistant`.
