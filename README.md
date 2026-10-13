# UB-WaveX 🎵

<div align="center">

![UB-WaveX Logo](wavexwhite.png)

**Music Reimagined**

A powerful, fast, and completely free desktop music streaming and downloading application.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://github.com/uselessbruh/UB-WaveX/releases)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://github.com/uselessbruh/UB-WaveX)

[Download](#-download) • [Features](#-features) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 🎯 What is UB-WaveX?

UB-WaveX is a full-featured desktop music application that lets you stream, download, and organize your favorite music with complete privacy. All operations are performed locally on your device - no cloud services, no tracking, no ads. Just pure music enjoyment.

### ✨ Why Choose UB-WaveX?

- **🔒 100% Private** - Everything runs locally on your device
- **💻 Offline Processing** - No backend servers, no data collection
- **✨ Completely Free** - Open source and free forever
- **🎵 High Quality** - Download in best available quality (up to 320kbps)
- **🎨 Modern UI** - Spotify-like interface with dark/light themes
- **📂 Smart Organization** - Playlists, liked songs, and powerful library management

## 📥 Download

Choose the version that matches your system:

### Windows Releases

| Version | Type | Size | Download |
|---------|------|------|----------|
| **Windows 64-bit** | Installer | 135.5 MB | [Download](https://github.com/uselessbruh/UB-WaveX/releases/latest/download/WaveX.Setup.1.0.0-x64.exe) ⭐ Recommended |
| **Windows 64-bit** | Portable ZIP | 171.4 MB | [Download](https://github.com/uselessbruh/UB-WaveX/releases/latest/download/WaveX-1.0.0-win-x64.zip) |
| **Windows 32-bit** | Installer | 124.6 MB | [Download](https://github.com/uselessbruh/UB-WaveX/releases/latest/download/WaveX.Setup.1.0.0-ia32.exe) |
| **Windows 32-bit** | Portable ZIP | 157.4 MB | [Download](https://github.com/uselessbruh/UB-WaveX/releases/latest/download/WaveX-1.0.0-win-ia32.zip) |

### Linux Releases (Coming Soon)

- AppImage (Universal)
- Debian/Ubuntu (.deb)

### System Requirements

- **OS**: Windows 10 or later
- **Memory**: 4GB RAM minimum
- **Storage**: 200MB free space
- **Network**: Internet connection for streaming

## 🚀 Features

## 🚀 Features

### Core Functionality

- 🔍 **Search & Stream** - Search and play music directly from YouTube
- ⬇️ **High-Quality Downloads** - Download tracks with embedded metadata and cover art (up to 320kbps)
- 📁 **Library Management** - Organize your music with downloads, liked songs, and custom playlists
- 🎵 **Smart Playback** - Automatic queue management with track preloading for seamless playback
- 🎨 **Modern UI** - Beautiful, responsive Spotify-like interface with dark and light themes
- 💾 **Offline Operation** - Runs entirely locally with no backend server required
- 🖼️ **Cover Art** - Automatic fetching and caching from Cover Art Archive
- 📊 **Metadata Resolution** - Enhanced metadata from MusicBrainz for accurate track information

### Advanced Features

- **Queue Management**: Tracks auto-play sequentially in playlists
- **Smart Preloading**: Next 5 tracks preload for uninterrupted playback
- **Playlist Support**: Create unlimited playlists, add/remove tracks
- **Search History**: Quick access to recent searches
- **Keyboard Controls**: Space to play/pause, arrow keys for seeking
- **Download Management**: Track download progress and manage your library

## 🎬 Quick Start

1. **Download** the installer for your platform from the [Download](#-download) section
2. **Install** the application (or extract the portable ZIP)
3. **Launch** UB-WaveX
4. **Search** for your favorite music and start playing!

No configuration needed - just install and enjoy your music!

## 📖 Documentation

### For Users

#### Search and Play Music

1. Enter a song name or artist in the search bar
2. Click **Search** or press Enter
3. Click on any track to play it immediately
4. Use the player controls at the bottom

#### Download Music

- Click the download icon (⬇️) on any track
- Downloaded tracks appear in the Downloads section
- All downloads include full metadata and cover art

#### Manage Your Library

**Downloads Section**:
- View all downloaded tracks
- Play offline without internet

**Liked Songs**:
- Click the heart icon (❤️) to like a track
- Access all liked songs in one place

**Playlists**:
- Create custom playlists with the **+** button
- Add tracks by right-clicking
- Download entire playlists at once

### For Developers

## 🛠️ Architecture

### Components

1. **Electron Frontend** - Desktop UI, playback controls, and database reads
2. **Python Core** (Packaged as EXE) - Music extraction, metadata resolution, downloads
3. **MySQL Database** - All persistent storage
4. **IPC Protocol** - JSON-based communication via STDIN/STDOUT

### Technology Stack

- **Frontend**: Electron, HTML5, CSS3, JavaScript
- **Backend**: Python 3.x with yt-dlp, requests, mysql-connector
- **Database**: MySQL 8.0+
- **Build Tools**: electron-builder, PyInstaller

## Prerequisites

### Required Software

1. **Node.js** (v18 or higher)
   - Download: https://nodejs.org/

2. **Python** (3.10 or higher)
   - Download: https://www.python.org/downloads/
   - Make sure to add Python to PATH during installation

3. **MySQL Server** (8.0 or higher)
   - Download: https://dev.mysql.com/downloads/mysql/
   - Note your root password during installation

4. **FFmpeg** (Required for yt-dlp audio conversion)
   - Download: https://ffmpeg.org/download.html
   - Add FFmpeg to system PATH

## Installation

### 1. Clone or Download the Project

```bash
cd C:\Users\ASUS\Desktop\UB-WaveX
```

### 2. Install Node Dependencies

```bash
npm install
```

### 3. Install Python Dependencies

```bash
cd src/python
pip install -r requirements.txt
cd ../..
```

### 4. Setup MySQL Database

1. Start MySQL server
2. Open MySQL command line or MySQL Workbench
3. Run the database schema:

```bash
mysql -u root -p < database/schema.sql
```

Or manually:
- Open MySQL Workbench
- Create a new connection to localhost
- Open `database/schema.sql`
- Execute the script

4. Update database credentials if needed in:
   - `src/electron/main.js` (lines 11-17)
   - `src/python/music_core.py` (lines 16-21)

### 5. Build Python Executable (Optional for Development)

For development, you can run the Python script directly. For production:

```bash
npm run build:python
```

This creates `src/python/dist/music_core.exe`

## Usage

### Development Mode

1. Start the application:

```bash
npm start
```

Or for development mode with debugging:

```bash
npm run dev
```

### Search and Play Music

1. Enter a song name or artist in the search bar
2. Click **Search** or press Enter
3. Click on any track to play it immediately
4. Use the player controls at the bottom

### Download Music

- Click the download icon (⬇️) on any track
- Or right-click and select "Download"
- Downloaded tracks appear in the Downloads section
- Downloads include full metadata and cover art

### Manage Library

**Downloads Section**:
- View all downloaded tracks
- Play offline without internet

**Liked Songs**:
- Click the heart icon (❤️) to like a track
- Access all liked songs in one place

**Playlists**:
- Click the **+** button to create a new playlist
- Click a playlist to view its tracks
- Right-click tracks to add to playlists
- Download entire playlists at once

### Playback Features

- **Queue Management**: Tracks auto-play sequentially in playlists
- **Preloading**: Next 5 tracks preload for seamless playback
- **Seek**: Click/drag the progress bar
- **Volume**: Adjust with the volume slider
- **Keyboard**: Press Space to play/pause

## Building for Distribution

### Build the Application

```bash
npm run build
```

This creates a Windows installer in the `dist` folder.

### Distribution Package Includes

- Electron application
- Python core executable
- All dependencies bundled
- Installer with optional installation directory

## Configuration

### Default Paths

- **Downloads**: `C:\Users\ASUS\Music\UB-WaveX`
- **Cache**: `C:\Users\ASUS\AppData\Local\UB-WaveX\cache`

These can be changed in the database `settings` table.

### Audio Quality

- Default: Best available (typically 320kbps MP3)
- Format: MP3 with embedded metadata and artwork

## Project Structure

```
UB-WaveX/
├── src/
│   ├── electron/
│   │   └── main.js              # Electron main process
│   ├── python/
│   │   ├── music_core.py        # Python core logic
│   │   ├── requirements.txt     # Python dependencies
│   │   └── music_core.spec      # PyInstaller config
│   └── ui/
│       ├── index.html           # Main UI
│       ├── styles.css           # Styling
│       ├── renderer.js          # UI logic
│       └── player.js            # Audio player engine
├── database/
│   └── schema.sql               # MySQL database schema
├── package.json                 # Node.js configuration
└── README.md                    # This file
```

## Troubleshooting

### Database Connection Failed

- Ensure MySQL server is running
- Check credentials in `src/electron/main.js` and `src/python/music_core.py`
- Verify database `ubwavex` exists

### Python Core Not Starting

- Ensure Python is in system PATH
- Check all Python dependencies are installed: `pip install -r src/python/requirements.txt`
- For packaged app, rebuild: `npm run build:python`

### FFmpeg Not Found

- Download FFmpeg from https://ffmpeg.org/
- Extract and add the `bin` folder to system PATH
- Restart terminal/command prompt after adding to PATH

### No Audio Playback

- Check internet connection (for streaming)
- Verify FFmpeg is installed
- Check browser console for errors (Ctrl+Shift+I)

### Search Returns No Results

- Verify internet connection
- Check if YouTube is accessible
- Try different search terms

## Database Schema

### Main Tables

- **tracks** - All music tracks
- **artists** - Artist information
- **albums** - Album information
- **downloads** - Downloaded track records
- **liked_songs** - User's liked tracks
- **playlists** - User playlists
- **playlist_tracks** - Playlist-track mappings
- **cache** - Metadata and stream URL cache
- **cover_art_cache** - Cached cover images

## Performance Optimization

### Caching Strategy

- Stream URLs cached for 6 hours
- Metadata cached for 30 days
- Cover images cached permanently
- Maximum 5 tracks preloaded in memory

### Database Optimization

- Indexed on frequently queried columns
- Foreign keys with appropriate cascading
- Connection pooling for efficiency

## License

MIT License - See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions from the community! UB-WaveX is open source, and we'd love your help to make it even better.

### Ways to Contribute

- 🐛 **Report Bugs** - Found a bug? [Open an issue](https://github.com/uselessbruh/UB-WaveX/issues)
- 💡 **Suggest Features** - Have an idea? We'd love to hear it!
- 📝 **Improve Documentation** - Help make our docs clearer
- 🔧 **Submit Pull Requests** - Fix bugs or add features
- 🌍 **Translations** - Help translate UB-WaveX to other languages
- ⭐ **Star the Repo** - Show your support!

### Development Setup

#### Prerequisites

1. **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
2. **Python** (3.10 or higher) - [Download](https://www.python.org/downloads/)
3. **MySQL Server** (8.0 or higher) - [Download](https://dev.mysql.com/downloads/mysql/)
4. **FFmpeg** - [Download](https://ffmpeg.org/download.html) and add to PATH

#### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/uselessbruh/UB-WaveX.git
cd UB-WaveX

# Install Node dependencies
npm install

# Install Python dependencies
cd src/python
pip install -r requirements.txt
cd ../..

# Setup MySQL database
mysql -u root -p < database/schema.sql

# Run in development mode
npm run dev
```

### Building from Source

```bash
# Build Python executable
npm run build:python

# Build Electron app
npm run build
```

This creates installers in the `dist` folder.

### Project Structure

```
UB-WaveX/
├── src/
│   ├── electron/
│   │   └── main.js              # Electron main process
│   ├── python/
│   │   ├── music_core.py        # Python core logic
│   │   ├── requirements.txt     # Python dependencies
│   │   └── music_core.spec      # PyInstaller config
│   └── ui/
│       ├── index.html           # Main UI
│       ├── styles.css           # Styling
│       ├── renderer.js          # UI logic
│       └── player.js            # Audio player engine
├── mainpage/                     # Website/landing page
├── database/
│   └── schema.sql               # MySQL database schema
├── package.json                 # Node.js configuration
└── README.md                    # This file
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please ensure:
- Code follows the existing style
- All tests pass
- Documentation is updated if needed
- Commit messages are clear and descriptive

## 🙏 Credits

## 🙏 Credits

This project is built with amazing open source technologies:

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube audio extraction
- **[MusicBrainz](https://musicbrainz.org/)** - Metadata resolution
- **[Cover Art Archive](https://coverartarchive.org/)** - Album artwork
- **[Electron](https://www.electronjs.org/)** - Desktop application framework
- **[Python](https://www.python.org/)** - Backend processing
- **[MySQL](https://www.mysql.com/)** - Database management

## 📞 Support

Need help or have questions?

- 📖 [Read the Documentation](#-documentation)
- 🐛 [Report an Issue](https://github.com/uselessbruh/UB-WaveX/issues)
- 💬 [Join Discussions](https://github.com/uselessbruh/UB-WaveX/discussions)
- 📧 Contact: [Create an issue](https://github.com/uselessbruh/UB-WaveX/issues)

## 🗺️ Roadmap

### Upcoming Features

- 🐧 Linux support (AppImage, .deb packages)
- 🎚️ Equalizer and audio effects
- 📱 Mobile companion app
- 🌐 Multi-language support
- 🔄 Cross-platform sync (optional, privacy-focused)
- 🎨 Customizable themes and UI layouts

### Community Requests

Have a feature request? [Open an issue](https://github.com/uselessbruh/UB-WaveX/issues) and let us know!

## ⚠️ Disclaimer

UB-WaveX is designed for personal use with music you have the right to access. Users are responsible for complying with copyright laws and YouTube's Terms of Service in their jurisdiction.

---

<div align="center">

**UB-WaveX** - Your personal music streaming and downloading companion

Made with ❤️ by the open source community

[⭐ Star on GitHub](https://github.com/uselessbruh/UB-WaveX) • [🐛 Report Bug](https://github.com/uselessbruh/UB-WaveX/issues) • [💡 Request Feature](https://github.com/uselessbruh/UB-WaveX/issues)

</div>
