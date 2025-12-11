
# from rest_framework import status
# from rest_framework.response import Response
# from django.http import HttpResponseRedirect
# from .upload_papers import supabase

# # Define your bucket name
# bucket_name = "files"
# folder_in_bucket = 'papers'

# def paper_download_redirect(paper):
    
#     try:
#       # Generate the temporary, pre-signed URL from Supabase
#       # The URL will be valid for a short duration (e.g., 60 seconds)
#       # to prevent unauthorized sharing of the download link.
      
#       # 'expiresIn': seconds the link remains valid (e.g., 60 seconds)
#       # 'download': forces the browser to download instead of displaying (important)
#       response = supabase.storage.from_(bucket_name).create_signed_url(
#       path=paper.file_link, 
#       expiresIn=60,
#       # Get the file name from the URL
#       options={
#             'download': paper.title # Set the download filename (i will modify the model to store the file name)
#       }
#       )
#       print(f"Response: {response}")

#       # Check for a valid URL in the response data
#       if 'signedURL' not in response:
#             print("Supabase Response:", response)
#             return Response({'error': 'Failed to generate download URL.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#       signed_url = response['signedURL']
#       print(f"Signed URL: "signed_url)

#       # Redirect the user's browser to the temporary URL
#       # The browser will then connect directly to Supabase storage to download the file.
#       return HttpResponseRedirect(signed_url)

#     except Exception as e:
#       print(f"Error generating Supabase URL for paper {paper.id}: {e}")
#       return Response({'error': 'Failed to generate download URL.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)