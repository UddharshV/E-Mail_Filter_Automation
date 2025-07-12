"""
Email Parser Utilities

This module provides functions to extract and parse email data from various sources.
It's designed to handle different email formats and extract relevant features for ML.
"""

import re
import email
from email import policy
from email import utils as email_utils
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import pandas as pd


class EmailParser:
    """Parser for extracting email features for machine learning."""
    
    def __init__(self):
        """Initialize the email parser."""
        self.policy = policy.default
        
    def parse_email_content(self, email_content: str) -> Dict:
        """
        Parse email content and extract features.
        
        Args:
            email_content: Raw email content as string
            
        Returns:
            Dictionary containing extracted features
        """
        try:
            # Parse email using email library
            msg = email.message_from_string(email_content, policy=self.policy)
            
            # Extract basic features
            features = {
                'subject': self._extract_subject(msg),
                'sender': self._extract_sender(msg),
                'recipients': self._extract_recipients(msg),
                'date': self._extract_date(msg),
                'content': self._extract_content(msg),
                'has_attachments': self._has_attachments(msg),
                'content_length': len(self._extract_content(msg)),
                'subject_length': len(self._extract_subject(msg)),
                'sender_domain': self._extract_domain(self._extract_sender(msg))
            }
            
            return features
            
        except Exception as e:
            print(f"Error parsing email: {e}")
            return {}
    
    def _extract_subject(self, msg) -> str:
        """Extract email subject."""
        subject = msg.get('subject', '')
        return subject if subject else 'No Subject'
    
    def _extract_sender(self, msg) -> str:
        """Extract sender email address."""
        sender = msg.get('from', '')
        # Extract email from "Name <email@domain.com>" format
        email_match = re.search(r'<(.+?)>', sender)
        if email_match:
            return email_match.group(1)
        return sender
    
    def _extract_recipients(self, msg) -> List[str]:
        """Extract recipient email addresses."""
        recipients = msg.get('to', '')
        if not recipients:
            return []
        
        # Split multiple recipients and clean
        email_list = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', recipients)
        return email_list
    
    def _extract_date(self, msg) -> Optional[datetime]:
        """Extract email date."""
        date_str = msg.get('date', '')
        if not date_str:
            return None
        
        try:
            # Parse various date formats
            parsed_date = email_utils.parsedate_to_datetime(date_str)
            return parsed_date
        except:
            return None
    
    def _extract_content(self, msg) -> str:
        """Extract email body content."""
        content = ""
        
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    content += part.get_content()
                    break
        else:
            content = msg.get_content()
        
        return content if content else ""
    
    def _has_attachments(self, msg) -> bool:
        """Check if email has attachments."""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_filename():
                    return True
        return False
    
    def _extract_domain(self, email_address: str) -> str:
        """Extract domain from email address."""
        if '@' in email_address:
            return email_address.split('@')[1]
        return ""
    
    def extract_features_for_ml(self, email_data: List[Dict]) -> pd.DataFrame:
        """
        Extract features from multiple emails for ML training.
        
        Args:
            email_data: List of dictionaries containing email data
            
        Returns:
            DataFrame with extracted features
        """
        features_list = []
        
        for email in email_data:
            features = self.parse_email_content(email.get('content', ''))
            features['filter_label'] = email.get('filter_label', 'unknown')
            features['email_id'] = email.get('id', '')
            features_list.append(features)
        
        return pd.DataFrame(features_list)


def clean_text(text: str) -> str:
    """
    Clean and normalize text content.
    
    Args:
        text: Raw text to clean
        
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters but keep spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def extract_keywords(text: str, top_n: int = 10) -> List[str]:
    """
    Extract most common keywords from text.
    
    Args:
        text: Text to analyze
        top_n: Number of top keywords to return
        
    Returns:
        List of top keywords
    """
    from collections import Counter
    
    # Clean text
    cleaned_text = clean_text(text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Remove common stop words (basic list)
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    words = [word for word in words if word not in stop_words and len(word) > 2]
    
    # Count frequency
    word_counts = Counter(words)
    
    # Return top N keywords
    return [word for word, count in word_counts.most_common(top_n)] 