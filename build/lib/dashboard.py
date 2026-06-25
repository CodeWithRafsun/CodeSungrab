#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.3
# Rich Download Dashboard
# ==========================================

from rich.console import Console
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TimeRemainingColumn,
    DownloadColumn,
    TransferSpeedColumn
)
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich import box
from config import Colors

console = Console()

# ==========================================
# Header Display
# ==========================================

def show_download_header(platform, media_type):
    """Show download header with Argentina flag"""
    text = (
        f"[bold cyan]SunGrab Mega v2.0.3[/bold cyan]\n"
        f"[white]Argentina Victory Edition 🇦🇷[/white]\n\n"
        f"[yellow]Platform:[/yellow] {platform}\n"
        f"[yellow]Type:[/yellow] {media_type}"
    )
    
    console.print(
        Panel(
            text,
            title="☀️ SunGrab",
            border_style="cyan"
        )
    )

# ==========================================
# Progress Bar
# ==========================================

def create_progress():
    """Create progress bar with Argentina colors"""
    progress = Progress(
        TextColumn("[bold sky_blue1]{task.description}"),
        BarColumn(bar_width=40, complete_style="sky_blue1", finished_style="white"),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console
    )
    return progress

def start_download_progress(description="Downloading..."):
    """Start download progress"""
    progress = create_progress()
    task = progress.add_task(description, total=100)
    return progress, task

def update_progress(progress, task, value):
    """Update progress"""
    progress.update(task, completed=value)

# ==========================================
# Status Display
# ==========================================

def show_complete(filename):
    """Show completion message"""
    console.print(
        Panel(
            f"[bold green]Download Completed Successfully![/bold green]\n\n"
            f"[white]File: {filename}[/white]",
            title="🇦🇷 Success",
            border_style="green"
        )
    )

def show_error(message):
    """Show error message"""
    console.print(
        Panel(
            f"[bold red]{message}[/bold red]",
            title="Error",
            border_style="red"
        )
    )

def show_info(message):
    """Show info message"""
    console.print(
        Panel(
            f"[bold cyan]{message}[/bold cyan]",
            title="Info",
            border_style="cyan"
        )
    )

# ==========================================
# Batch Status Display
# ==========================================

def show_batch_status(current, total, url):
    """Show batch download status"""
    console.print(
        f"[bold sky_blue1]Batch Progress:[/bold sky_blue1] "
        f"[white]{current}/{total}[/white] "
        f"[dim]- {url}[/dim]"
    )

def show_batch_summary(results):
    """Show batch download summary"""
    total = len(results)
    success = sum(1 for _, r in results if r)
    failed = total - success
    
    table = Table(title="Batch Download Summary", box=box.ROUNDED)
    table.add_column("Status", style="cyan")
    table.add_column("Count", style="white")
    table.add_column("Percentage", style="white")
    
    table.add_row("✅ Success", str(success), f"{success/total*100:.1f}%")
    if failed > 0:
        table.add_row("❌ Failed", str(failed), f"{failed/total*100:.1f}%")
    table.add_row("📊 Total", str(total), "100%")
    
    console.print(table)

# ==========================================
# Playlist Info Display
# ==========================================

def show_playlist_info(info):
    """Show playlist information"""
    title = info.get("title", "Unknown Playlist")
    count = info.get("playlist_count", 0)
    
    console.print(
        Panel(
            f"[bold cyan]Playlist:[/bold cyan] {title}\n"
            f"[bold white]Videos:[/bold white] {count}",
            title="🎬 Playlist Info",
            border_style="cyan"
        )
    )
    return count
