#!/usr/bin/env python3

# ==========================================
# SunGrab Mega v2.0.2
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


console = Console()


def show_download_header(platform, media_type):

    text = (
        f"[bold cyan]SunGrab Mega v2.0.2[/bold cyan]\n"
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


def create_progress():

    progress = Progress(
        TextColumn(
            "[bold blue]{task.description}"
        ),

        BarColumn(
            bar_width=40
        ),

        DownloadColumn(),

        TransferSpeedColumn(),

        TimeRemainingColumn()
    )

    return progress



def start_download_progress(
        description="Downloading..."
):

    progress = create_progress()

    task = progress.add_task(
        description,
        total=100
    )

    return progress, task



def update_progress(
        progress,
        task,
        value
):

    progress.update(
        task,
        completed=value
    )



def show_complete(filename):

    console.print(
        Panel(
            f"[bold green]"
            f"Download Completed Successfully\n\n"
            f"File: {filename}"
            f"[/bold green]",
            title="🇦🇷 Success",
            border_style="green"
        )
    )



def show_error(message):

    console.print(
        Panel(
            f"[bold red]{message}[/bold red]",
            title="Error",
            border_style="red"
        )
    )
