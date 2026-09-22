# GitHub access via SSH deploy key

Scoped to this repo only — the key can't access any other repo on the account.

1. Generate a dedicated key pair:
   ```
   ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_smart_home -C "smart-home deploy key (work laptop)"
   ```
2. Add to `~/.ssh/config`:
   ```
   Host github-smart-home
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_ed25519_smart_home
       IdentitiesOnly yes
   ```
3. Point the repo's remote at it:
   ```
   git remote set-url origin git@github-smart-home:guycohen85/smart-home.git
   ```
4. On GitHub: repo `Settings > Deploy keys > Add deploy key` — paste the contents of `id_ed25519_smart_home.pub`, check **Allow write access**.
5. Verify:
   ```
   ssh -T git@github-smart-home
   git fetch origin
   ```
