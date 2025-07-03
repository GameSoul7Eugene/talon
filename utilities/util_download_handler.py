import os
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from .util_ssl import create_ssl_context
from utilities.util_logger import logger
from utilities.util_error_popup import show_error_popup



def download_file(
    url: str, dest_name: str | None = None, retries: int = 3
) -> bool:
    temp_dir = os.environ.get('TEMP', tempfile.gettempdir())
    download_dir = os.path.join(temp_dir, 'talon')
    try:
        os.makedirs(download_dir, exist_ok=True)
    except Exception as e:
        logger.error(f"Failed to create download directory {download_dir}: {e}")
        show_error_popup(f"Failed to create download directory:\n{e}", allow_continue=True)
        return False
    if dest_name is None:
        try:
            parsed = urllib.parse.urlparse(url)
            filename = os.path.basename(parsed.path)
            if not filename:
                raise ValueError("No filename found in URL path")
        except Exception as e:
            logger.error(f"Could not determine filename from URL {url}: {e}")
            show_error_popup(
                f"Could not determine filename from URL:\n{url}\n{e}",
                allow_continue=True,
            )
            return False
    else:
        filename = dest_name
    dest_path = os.path.join(download_dir, filename)
    ssl_context = create_ssl_context()
    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Attempt {attempt}/{retries}: Downloading {url} to {dest_path}")
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, context=ssl_context) as response, open(dest_path, "wb") as out_file:
                out_file.write(response.read())
            logger.info(f"Successfully downloaded {url} to {dest_path}")
            return True
        except Exception as e:
            logger.warning(f"Download attempt {attempt} failed: {e}")
            if attempt == retries:
                logger.error(f"Failed to download {url} after {retries} attempts")
                show_error_popup(f"Failed to download:\n{url}\nafter {retries} attempts", allow_continue=True)
                return False
    return False
