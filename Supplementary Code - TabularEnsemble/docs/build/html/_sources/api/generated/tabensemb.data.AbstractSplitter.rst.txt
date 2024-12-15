tabensemb.data.AbstractSplitter
===============================

.. currentmodule:: tabensemb.data

.. autoclass:: AbstractSplitter
   :show-inheritance:
   
   .. rubric:: Methods
   .. automethod:: __init__

   
   .. autosummary::
   
      ~AbstractSplitter.reset_cv
      ~AbstractSplitter.split
   
      ~AbstractSplitter._check_exist
      ~AbstractSplitter._check_split
      ~AbstractSplitter._next_cv
      ~AbstractSplitter._sklearn_k_fold
      ~AbstractSplitter._split
   

   


   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         AbstractSplitter._check_exist
         AbstractSplitter._check_split
         AbstractSplitter._next_cv
         AbstractSplitter._sklearn_k_fold
         AbstractSplitter._split
         AbstractSplitter.reset_cv
         AbstractSplitter.split



   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         AbstractSplitter.support_cv
