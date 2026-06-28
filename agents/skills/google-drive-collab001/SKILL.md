---
name: google-drive-collab001
description: Interact with Google Drive scoped to the collab001 project folder. List, search, read, upload, and download files — all operations are restricted to the collab001 folder. Uses a service account that has been granted access to the folder.
---

# Google Drive — collab001 Folder

## When to Use

- The user wants to list, search, read, upload, or download files in Google Drive
- The user references a document, spreadsheet, or file by name
- The user wants to save or retrieve project artifacts

## Authentication

This skill uses a **service account** (not OAuth). The service account email must be shared on the collab001 folder in Google Drive. If the user reports permission errors, remind them to share the folder with the service account email.

## Folder Constraint

You MUST restrict all Drive operations to the `collab001` folder:

- **Folder ID:** `1oMBRuG-5pQxD0pGs9HyuUqKKiDPXs7cI`

## Operations

### Listing files

Use the query `'1oMBRuG-5pQxD0pGs9HyuUqKKiDPXs7cI' in parents` to list only files within the collab001 folder.

### Searching files

Include `'1oMBRuG-5pQxD0pGs9HyuUqKKiDPXs7cI' in parents` as a filter in your search query so results stay within the collab001 folder.

### Uploading files

Always specify the collab001 folder ID as the parent folder so uploads land in the right place.

### Reading / downloading files

Only read or download files that belong to the collab001 folder.

## Key Rules

- Never access, list, search, upload to, or download from any Drive location outside the collab001 folder.
- If you get a permission error, the collab001 folder likely needs to be shared with the service account email.
- If the user asks about files outside collab001, explain that your Drive access is scoped to the project folder only.
